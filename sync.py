import os
import shutil
import argparse


def copy_dir(src: str, dst: str) -> None:
    if not os.path.exists(src):
        print(f"[WARN] Source directory does not exist: {src}")
        return

    if os.path.exists(dst):
        shutil.rmtree(dst)

    shutil.copytree(src, dst)
    print(f"[OK] Copied directory: {src} -> {dst}")


def copy_file(src: str, dst: str) -> None:
    if not os.path.exists(src):
        print(f"[WARN] Source file does not exist: {src}")
        return

    dst_parent = os.path.dirname(dst)
    if dst_parent:
        os.makedirs(dst_parent, exist_ok=True)

    shutil.copy2(src, dst)
    print(f"[OK] Copied file: {src} -> {dst}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Sync agents, skills, and Codex config.toml"
    )
    parser.add_argument(
        "mode",
        choices=["fetch", "push"],
        help="Mode: fetch or push",
    )
    parser.add_argument(
        "--agents-path",
        required=True,
        help="Path to agents folder",
    )
    parser.add_argument(
        "--skills-path",
        required=True,
        help="Path to skills folder",
    )
    parser.add_argument(
        "--config-path",
        default="/home/hoang/.codex/config.toml",
        help="Path to Codex config.toml",
    )

    args = parser.parse_args()

    local_agents = os.path.abspath("./agents")
    local_skills = os.path.abspath("./skills")
    local_config = os.path.abspath("./config.toml")

    if args.mode == "fetch":
        # Copy from source paths into local project
        copy_dir(args.agents_path, local_agents)
        copy_dir(args.skills_path, local_skills)
        copy_file(args.config_path, local_config)

    elif args.mode == "push":
        # Copy from local project back to source paths
        copy_dir(local_agents, args.agents_path)
        copy_dir(local_skills, args.skills_path)
        copy_file(local_config, args.config_path)


if __name__ == "__main__":
    main()