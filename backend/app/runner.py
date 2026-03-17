import asyncio
import re

async def run_sherlock(username: str):
    """
    Asynchronously executes Sherlock for a given username and yields each found URL.
    """
    # Using 'sherlock' from pip
    cmd = ["sherlock", username, "--no-color", "--print-found", "--nsfw", "--no-txt"]
    
    process = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    # Regex to extract [SiteName]: [URL] pattern from Sherlock output
    # Example: [*] GitHub: https://github.com/username
    result_pattern = re.compile(r"\[\+\]\s+(?P<site>[^:]+):\s+(?P<url>https?://\S+)")

    while True:
        line = await process.stdout.readline()
        if not line:
            break
        
        decoded_line = line.decode().strip()
        match = result_pattern.search(decoded_line)
        if match:
            yield {
                "site": match.group("site").strip(),
                "url": match.group("url").strip()
            }

    await process.wait()
