---
type: summary
source: 01_Raw/anthropic.com/research/confidential-inference-trusted-vms.md
source_url: https://www.anthropic.com/research/confidential-inference-trusted-vms
title: "Confidential Inference via Trusted Virtual Machines"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Anthropic 正在研究并构建"机密推理"（Confidential Inference）技术，通过密码学手段在硬件层面保证用户数据和模型权重的安全性。

**核心目标**：机密推理有两大用途——保护模型权重免遭威胁行为者窃取，以及通过可验证的方式证明用户敏感数据始终在加密状态下处理。

**技术架构**：推理服务分为 API Server 和 Inference Server 两部分。Inference Server 内设一个"可信加载器"（trusted loader），运行在由 hypervisor 隔离的独立虚拟机中，作为"虚拟加速器"对外呈现。只有经过安全 CI 服务器签名的程序才能在加载器中运行，需多名工程师审核。

**可信环境的三个特征**：（1）硬件加密内存，隔离于其他工作负载；（2）禁用调试功能；（3）通过可信平台模块（TPM）提供密码学证明，确保运行的是正确且经过审查的代码。密钥服务器仅在验证证明后才释放解密密钥。

**数据流保护**：用户请求在到达 Anthropic 服务器之前即被加密；经 API Server 解密、处理、再加密后传递给 Inference Server；仅在发送至可信加载器时才解密；响应在离开加载器前再次加密。模型权重同样仅在加载器内解密，从不向外释放。

**未来方向**：考虑在加载器层面加入出口带宽限制，或要求安全分类器签名才能运行推理；希望硬件设计者将机密计算整合进加速器芯片，从而大幅缩小信任边界。该研究为初步探索，系与 Pattern Labs 合作发布。
