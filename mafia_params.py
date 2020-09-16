from lang import english, persian
from config import load_data

max_comments : int = lambda nPlayers : nPlayers // 3

data = load_data("mafia_param.json")

ordered_roles = data.get("ordered_roles")
nRoles = data.get("nRoles")
role2team = data.get("role2team")