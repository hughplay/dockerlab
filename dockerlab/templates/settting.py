DEFAULT_TEMPLATE = "workspace_base"

TEMPLATE_SETTING = {
    "workspace_base": {
        "post_templates": ["python", "default"],
        "assets": ["misc/", "requirements.txt"],
        "cuda": "",
        "prebuilt": "deepbase/dockerlab:workspace_base",
    },
    "workspace_cuda_11_1": {
        "post_templates": ["python", "default"],
        "assets": ["misc/", "requirements.txt"],
        "cuda": "11.1",
        "prebuilt": "deepbase/dockerlab:workspace_cuda_11_1",
    },
    "workspace_cuda_11_3": {
        "post_templates": ["python", "default"],
        "assets": ["misc/", "requirements.txt"],
        "cuda": "11.3",
        "prebuilt": "deepbase/dockerlab:workspace_cuda_11_3",
    },
    "workspace_cuda_11_7": {
        "post_templates": ["python", "default"],
        "assets": ["misc/", "requirements.txt"],
        "cuda": "11.7",
        "prebuilt": "deepbase/dockerlab:workspace_cuda_11_7",
    },
    "runtime_node_lts": {
        "post_templates": ["node", "default"],
        "assets": ["misc/"],
        "cuda": "",
        "prebuilt": "deepbase/dockerlab:runtime_node_lts",
    },
    "workspace_pytorch_1_13": {
        "post_templates": ["python", "default"],
        "assets": ["misc/", "requirements.txt"],
        "cuda": "11.7",
        "prebuilt": "deepbase/dockerlab:workspace_pytorch_1_13",
    },
    "workspace_pytorch_2_0": {
        "post_templates": ["python", "default"],
        "assets": ["misc/", "requirements.txt"],
        "cuda": "11.7",
        "prebuilt": "deepbase/dockerlab:workspace_pytorch_2_0",
    },
    "workspace_protein": {
        "post_templates": ["python", "default"],
        "assets": ["misc/", "requirements.txt"],
        "cuda": "11.1",
        "prebuilt": "deepbase/dockerlab:workspace_protein",
    },
}
