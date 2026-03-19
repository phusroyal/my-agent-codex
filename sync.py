import os
import shutil
import argparse

def copy_dir(src, dst):
    if not os.path.exists(src):
        print(f"[WARN] Source does not exist: {src}")
        return
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    print(f"[OK] Copied {src} -> {dst}")

def main():
    parser = argparse.ArgumentParser(description="Sync agents/skills folders")
    parser.add_argument("mode", choices=["fetch", "push"], help="Mode: fetch or push")
    parser.add_argument("--agents-path", required=True, help="Path to agents folder")
    parser.add_argument("--skills-path", required=True, help="Path to skills folder")

    args = parser.parse_args()

    local_agents = os.path.abspath("./agents")
    local_skills = os.path.abspath("./skills")

    if args.mode == "fetch":
        # copy from source paths into local project
        copy_dir(args.agents_path, local_agents)
        copy_dir(args.skills_path, local_skills)

    elif args.mode == "push":
        # copy from local project back to source paths
        copy_dir(local_agents, args.agents_path)
        copy_dir(local_skills, args.skills_path)

if __name__ == "__main__":
    main()