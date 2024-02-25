import asyncio
from src.bot import challenge_player

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(challenge_player())
