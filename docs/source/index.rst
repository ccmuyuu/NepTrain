.. NepTrainKit documentation master file, created by
   sphinx-quickstart on Wed Dec  4 19:50:15 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

NepTrain documentation
=========================
NepTrain 是一款专门设计的自动化训练 NEP（神经网络势）工具包。该工具包本身不直接进行计算，而是通过调用 GPUMD、NEP 和 VASP 等外部软件完成实际的计算任务。它支持多种功能，包括但不限于：

微扰：自动生成微扰数据，用于扩展训练集和提升模型的鲁棒性。
主动学习：利用最远点采样方法自动筛选训练样本，提升模型效率和准确性。
单点能计算：快速计算单点能，为训练提供高质量参考数据。
势函数训练：支持对 NEP 势的高效训练，优化性能和精度。
用户可以通过灵活的 子命令 调用实现自定义任务，也可以直接调用其 自动训练 功能，一键完成从样本生成到模型优化的全流程工作。

NepTrain 的设计目标是简化 NEP 的训练过程，提升用户的科研效率，使得训练集构建变得更加便捷和高效。


.. toctree::
   :maxdepth: 2
   :caption: Documentation:

   install    <install/index>
   command    <command/index>



