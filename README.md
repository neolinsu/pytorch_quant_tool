# pytorch_quant_tool
An experimental neural network quantization environment in Pytorch.

## Post Training Quantization
* NOTE: Fuse the well-trained model before operating *Post Training Quantization*.

### fuse_model(model, rules, inplace=True):
Fuse the model with a list of rules.
* Args:
    * model: A nn.Module to be fused.
    * rules: A list of rule object functions as FuseRule.
    * inplace: Bool. If True, the model object will be modified.
* Return:
    * A new fused model, if inplace is False.

### post_training_quant
Quant a trained model (int8).
* Args:
    * model: A fused nn.Module to be quanted.
    * data_loader: A data loader provides input data iterations.
    * batches: The limitation of iteration(batch) number.
    *inplace: Bool. If True, the model object will be modified.
* Return:
    A new quanted model, if inplace is False.
