from collections import Counter
import sys

def analyze_log(file_name):
    try:
        with open(file_name, 'r') as file:
            # Extract User Agent strings from the access log
            user_agents = [line.split('"')[5] for line in file if len(line.split('"')) > 5]
            user_agent_counts = Counter(user_agents)

            # Display the total unique User Agents count
            print(f"Total unique User Agents: {len(user_agent_counts)}")
            
            # Display the count of requests for each User Agent
            for agent, count in user_agent_counts.items():
                print(f"{agent}: {count}")
    except FileNotFoundError:
        print("Error: File not found. Please check the file name and try again.")
    except IndexError:
        print("Error: Log file format may be incorrect.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 access_log_analyzer.py <log_file>")
    else:
        analyze_log(sys.argv[1])

