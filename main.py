import json

vdp_params = object()
with open("./config.json") as f:
    vdp_params = json.load(f)

make_sets(vdp_params)