import os
import csv
import glob

builder_lines = []
final_lines = ["FROM base-tools AS final", ""]
seen_actions = set()

# Find all manifests across all lab subdirectories
manifest_paths = sorted(glob.glob("labs/**/software-manifest.csv", recursive=True))

##generate the base-tools layer

builder_lines.append(f"# ==========================================")
builder_lines.append(f"# STAGE: base-tools")
builder_lines.append(f"# ==========================================")
builder_lines.append(f"FROM ubuntu:24.04 AS base-tools")
builder_lines.append(f"WORKDIR /build/base-tools")

builder_lines.append(f"COPY base-install.sh /tmp/base-install.sh")
builder_lines.append(f"RUN chmod +x /tmp/base-install.sh && /tmp/base-install.sh")
builder_lines.append("")


for manifest_path in manifest_paths:
    # Extract the lab name from the path (e.g., 'labs/lab_x/...' -> 'lab_x')
    path_parts = manifest_path.split(os.sep)
    try:
        labs_idx = path_parts.index("labs")
        lab_name = path_parts[labs_idx + 1]
    except (ValueError, IndexError):
        lab_name = "unknown-lab"

    install_dir = os.path.dirname(manifest_path)

    # 1. Generate the intermediate builder stage for this lab
    builder_lines.append(f"# ==========================================")
    builder_lines.append(f"# STAGE: {lab_name}")
    builder_lines.append(f"# ==========================================")
    builder_lines.append(f"FROM base-tools AS {lab_name}")
    builder_lines.append(f"WORKDIR /build/{lab_name}")
    # Copy the lab's installation folder into a temporary build spot and execute its install script
    builder_lines.append(f"COPY {install_dir} /tmp/install-{lab_name}")
    builder_lines.append(f"RUN chmod +x /tmp/install-{lab_name}/software-install.sh && /tmp/install-{lab_name}/software-install.sh")
    builder_lines.append("")

    # 2. Parse the manifest to queue up the final assembly instructions
    with open(manifest_path, mode="r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            art_type = row["type"]
            source = row["source"]
            filename = os.path.basename(source)

            # Deduplication check to prevent redundant copy actions
            if art_type == "directory":
                action_key = (lab_name, source, source)
                if action_key not in seen_actions:
                    seen_actions.add(action_key)
                    final_lines.append(f"COPY --from={lab_name} {source} {source}")
            elif art_type == "file":
                action_key = (lab_name, source, "/usr/local/bin/")
                if action_key not in seen_actions:
                    seen_actions.add(action_key)
                    final_lines.append(f"COPY --from={lab_name} {source} /usr/local/bin/")
            elif art_type == "symlink":
                action_key = (lab_name, source, f"/usr/local/bin/{filename}")
                if action_key not in seen_actions:
                    seen_actions.add(action_key)
                    final_lines.append(f"RUN ln -s {source} /usr/local/bin/{filename}")

# Finalize the assembly stage cleanup and entrypoint
final_lines.append("RUN apt-get clean && rm -rf /var/lib/apt/lists/*")
final_lines.append('WORKDIR /root')
final_lines.append('CMD ["bash"]')

# Merge builder stages and final stage into one file
complete_dockerfile = builder_lines + final_lines

with open("Dockerfile.generated", "w") as f:
    f.write("\n".join(complete_dockerfile))

print("Successfully generated complete Dockerfile.generated from all lab directories!")