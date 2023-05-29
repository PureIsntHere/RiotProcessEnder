import psutil

riotProc = ["RiotClientServices.exe" , "LeagueClient.exe", "LeagueClientUx.exe", "LeagueClientUxRenderer.exe","LeagueCrashHandler64.exe","RiotClientServices.exe"]
procCount = 0
for process in psutil.process_iter():
    if process.name() in riotProc:
        procCount += 1
        process.kill()
print(f"Killed:{procCount} Riot Processes")