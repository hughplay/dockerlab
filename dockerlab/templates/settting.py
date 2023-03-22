DEFAULT_TEMPLATE = "workspace_base"
TEMPLATE_SETTING = {
    "workspace_base": {
        "post_templates": ["python", "default"],
        "assets": ["misc/", "requirements.txt"],
    },
    "workspace_cuda_11_1": {
        "post_templates": ["python", "default"],
        "assets": ["misc/", "requirements.txt"],
    },
    "workspace_cuda_11_7": {
        "post_templates": ["python", "default"],
        "assets": ["misc/", "requirements.txt"],
    },
    "runtime_node_lts": {
        "post_templates": ["node", "default"],
        "assets": ["misc/"],
    },
    "workspace_pytorch_1_13": {
        "post_templates": ["python", "default"],
        "assets": ["misc/", "requirements.txt"],
    },
    "workspace_pytorch_2_0": {
        "post_templates": ["python", "default"],
        "assets": ["misc/", "requirements.txt"],
    },
    "workspace_protein": {
        "post_templates": ["python", "default"],
        "assets": ["misc/", "requirements.txt"],
    },
}
PREBUILT_TEMPLATES = {
    "workspace_base": "deepbase/dockerlab:workspace_base",
    "workspace_cuda_11_1": "deepbase/dockerlab:workspace_cuda_11_1",
    "workspace_cuda_11_7": "deepbase/dockerlab:workspace_cuda_11_7",
    "runtime_node_lts": "deepbase/dockerlab:runtime_node_lts",
    "workspace_pytorch_1_13": "deepbase/dockerlab:workspace_pytorch_1_13",
    "workspace_pytorch_2_0": "deepbase/dockerlab:workspace_pytorch_2_0",
    "workspace_protein": "deepbase/dockerlab:workspace_protein",
}
