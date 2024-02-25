import os
from dotenv import load_dotenv
from poke_env import ShowdownServerConfiguration, AccountConfiguration
from poke_env.player import RandomPlayer

load_dotenv()

async def challenge_player(name: str):
    account_config = AccountConfiguration(os.getenv("TOBETHEBEST_BOT_USERNAME"), os.getenv("TOBETHEBEST_BOT_PASSWORD"))
    player = RandomPlayer(
        server_configuration=ShowdownServerConfiguration,
        account_configuration=account_config,
    )

    await player.send_challenges(name, n_challenges=1)

