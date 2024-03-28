import sys
import subprocess

def execute_git_command(command, repo_dir, branch1, branch2):
    commands = ["git","diff",branch1, branch2]
    try:
        result = subprocess.run(
            commands, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
            text=True,
            cwd=repo_dir
        )
        
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            print("Error executing Git command:")
            print(result.stderr.strip())
            return None
        
    except Exception as e:
        print("Exception:", e)
        return None

# git_command = "git status"  
# repo_dir = "C://Users//Lenovo//Desktop//automation-scripts"

if __name__ == '__main__':
    commands = sys.argv
    git_command = sys.argv[1]
    repo_dir = sys.argv[2]
    branch1 = sys.argv[3]
    branch2 = sys.argv[4]
    output = execute_git_command(git_command, repo_dir, branch1, branch2)
    if output is not None:
        print(output)