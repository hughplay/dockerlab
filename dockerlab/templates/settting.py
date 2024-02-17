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
    "workspace_cuda_11_8": {
        "post_templates": ["python", "default"],
        "assets": ["misc/", "requirements.txt"],
        "cuda": "11.8",
        "prebuilt": "deepbase/dockerlab:workspace_cuda_11_8",
    },
    "workspace_cuda_12_1": {
        "post_templates": ["python", "default"],
        "assets": ["misc/", "requirements.txt"],
        "cuda": "12.1",
        "prebuilt": "deepbase/dockerlab:workspace_cuda_12_1",
    },
    "runtime_node_lts": {
        "post_templates": ["node", "default"],
        "assets": ["misc/"],
        "cuda": "",
        "prebuilt": "deepbase/dockerlab:runtime_node_lts",
    },
    "workspace_node_16": {
        "post_templates": ["node", "default"],
        "assets": ["misc/"],
        "cuda": "",
        "prebuilt": "deepbase/dockerlab:workspace_node_16",
    },
    "workspace_node_18": {
        "post_templates": ["node", "default"],
        "assets": ["misc/"],
        "cuda": "",
        "prebuilt": "deepbase/dockerlab:workspace_node_18",
    },
    "workspace_node_20": {
        "post_templates": ["node", "default"],
        "assets": ["misc/"],
        "cuda": "",
        "prebuilt": "deepbase/dockerlab:workspace_node_20",
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
    "workspace_pytorch_2_1": {
        "post_templates": ["python", "default"],
        "assets": ["misc/", "requirements.txt"],
        "cuda": "12.1",
        "prebuilt": "deepbase/dockerlab:workspace_pytorch_2_1",
    },
    "workspace_pytorch_2_2": {
        "post_templates": ["python", "default"],
        "assets": ["misc/", "requirements.txt"],
        "cuda": "12.1",
        "prebuilt": "deepbase/dockerlab:workspace_pytorch_2_2",
    },
    "workspace_protein": {
        "post_templates": ["python", "default"],
        "assets": ["misc/", "requirements.txt"],
        "cuda": "11.1",
        "prebuilt": "deepbase/dockerlab:workspace_protein",
    },
}
