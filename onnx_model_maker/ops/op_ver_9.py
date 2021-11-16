# Autogenerated by onnx-model-maker. Don't modify it manually.

import onnx
import onnx.helper
import onnx.numpy_helper
from onnx_model_maker import omm
from onnx_model_maker import onnx_mm_export
from onnx_model_maker.ops.op_helper import _add_input


@onnx_mm_export("v9.MeanVarianceNormalization")
def MeanVarianceNormalization(X, **kwargs):
  _inputs = []
  for i in (X, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["MeanVarianceNormalization"]
  omm.op_counter["MeanVarianceNormalization"] += 1
  node = onnx.helper.make_node("MeanVarianceNormalization",
                               _inputs, [f'_t_MeanVarianceNormalization_{idx}_Y'],
                               name=f"MeanVarianceNormalization_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v9.TfIdfVectorizer")
def TfIdfVectorizer(X, **kwargs):
  _inputs = []
  for i in (X, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["TfIdfVectorizer"]
  omm.op_counter["TfIdfVectorizer"] += 1
  node = onnx.helper.make_node("TfIdfVectorizer",
                               _inputs, [f'_t_TfIdfVectorizer_{idx}_Y'],
                               name=f"TfIdfVectorizer_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v9.NonZero")
def NonZero(X, **kwargs):
  _inputs = []
  for i in (X, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["NonZero"]
  omm.op_counter["NonZero"] += 1
  node = onnx.helper.make_node("NonZero",
                               _inputs, [f'_t_NonZero_{idx}_Y'],
                               name=f"NonZero_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v9.Sign")
def Sign(input, **kwargs):
  _inputs = []
  for i in (input, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Sign"]
  omm.op_counter["Sign"] += 1
  node = onnx.helper.make_node("Sign",
                               _inputs, [f'_t_Sign_{idx}_output'],
                               name=f"Sign_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v9.IsNaN")
def IsNaN(X, **kwargs):
  _inputs = []
  for i in (X, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["IsNaN"]
  omm.op_counter["IsNaN"] += 1
  node = onnx.helper.make_node("IsNaN",
                               _inputs, [f'_t_IsNaN_{idx}_Y'],
                               name=f"IsNaN_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v9.Shrink")
def Shrink(input, **kwargs):
  _inputs = []
  for i in (input, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Shrink"]
  omm.op_counter["Shrink"] += 1
  node = onnx.helper.make_node("Shrink",
                               _inputs, [f'_t_Shrink_{idx}_output'],
                               name=f"Shrink_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v9.Sinh")
def Sinh(input, **kwargs):
  _inputs = []
  for i in (input, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Sinh"]
  omm.op_counter["Sinh"] += 1
  node = onnx.helper.make_node("Sinh",
                               _inputs, [f'_t_Sinh_{idx}_output'],
                               name=f"Sinh_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v9.Scatter")
def Scatter(data, indices, updates, **kwargs):
  _inputs = []
  for i in (data, indices, updates):
    _add_input(i, _inputs)

  idx = omm.op_counter["Scatter"]
  omm.op_counter["Scatter"] += 1
  node = onnx.helper.make_node("Scatter",
                               _inputs, [f'_t_Scatter_{idx}_output'],
                               name=f"Scatter_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v9.OneHot")
def OneHot(indices, depth, values, **kwargs):
  _inputs = []
  for i in (indices, depth, values):
    _add_input(i, _inputs)

  idx = omm.op_counter["OneHot"]
  omm.op_counter["OneHot"] += 1
  node = onnx.helper.make_node("OneHot",
                               _inputs, [f'_t_OneHot_{idx}_output'],
                               name=f"OneHot_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v9.MaxUnpool")
def MaxUnpool(X, I, output_shape=None, **kwargs):
  _inputs = []
  for i in (X, I, output_shape):
    _add_input(i, _inputs)

  idx = omm.op_counter["MaxUnpool"]
  omm.op_counter["MaxUnpool"] += 1
  node = onnx.helper.make_node("MaxUnpool",
                               _inputs, [f'_t_MaxUnpool_{idx}_output'],
                               name=f"MaxUnpool_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v9.EyeLike")
def EyeLike(input, **kwargs):
  _inputs = []
  for i in (input, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["EyeLike"]
  omm.op_counter["EyeLike"] += 1
  node = onnx.helper.make_node("EyeLike",
                               _inputs, [f'_t_EyeLike_{idx}_output'],
                               name=f"EyeLike_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v9.ConstantOfShape")
def ConstantOfShape(input, **kwargs):
  _inputs = []
  for i in (input, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["ConstantOfShape"]
  omm.op_counter["ConstantOfShape"] += 1
  node = onnx.helper.make_node("ConstantOfShape",
                               _inputs, [f'_t_ConstantOfShape_{idx}_output'],
                               name=f"ConstantOfShape_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v9.Compress")
def Compress(input, condition, **kwargs):
  _inputs = []
  for i in (input, condition):
    _add_input(i, _inputs)

  idx = omm.op_counter["Compress"]
  omm.op_counter["Compress"] += 1
  node = onnx.helper.make_node("Compress",
                               _inputs, [f'_t_Compress_{idx}_output'],
                               name=f"Compress_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v9.Scan")
def Scan(initial_state_and_scan_inputs, **kwargs):
  _inputs = []
  for i in (initial_state_and_scan_inputs, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Scan"]
  omm.op_counter["Scan"] += 1
  node = onnx.helper.make_node("Scan",
                               _inputs, [f'_t_Scan_{idx}_final_state_and_scan_outputs'],
                               name=f"Scan_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v9.Upsample")
def Upsample(X, scales, **kwargs):
  _inputs = []
  for i in (X, scales):
    _add_input(i, _inputs)

  idx = omm.op_counter["Upsample"]
  omm.op_counter["Upsample"] += 1
  node = onnx.helper.make_node("Upsample",
                               _inputs, [f'_t_Upsample_{idx}_Y'],
                               name=f"Upsample_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v9.Acosh")
def Acosh(input, **kwargs):
  _inputs = []
  for i in (input, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Acosh"]
  omm.op_counter["Acosh"] += 1
  node = onnx.helper.make_node("Acosh",
                               _inputs, [f'_t_Acosh_{idx}_output'],
                               name=f"Acosh_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v9.Where")
def Where(condition, X, Y, **kwargs):
  _inputs = []
  for i in (condition, X, Y):
    _add_input(i, _inputs)

  idx = omm.op_counter["Where"]
  omm.op_counter["Where"] += 1
  node = onnx.helper.make_node("Where",
                               _inputs, [f'_t_Where_{idx}_output'],
                               name=f"Where_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v9.Erf")
def Erf(input, **kwargs):
  _inputs = []
  for i in (input, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Erf"]
  omm.op_counter["Erf"] += 1
  node = onnx.helper.make_node("Erf",
                               _inputs, [f'_t_Erf_{idx}_output'],
                               name=f"Erf_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v9.Asinh")
def Asinh(input, **kwargs):
  _inputs = []
  for i in (input, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Asinh"]
  omm.op_counter["Asinh"] += 1
  node = onnx.helper.make_node("Asinh",
                               _inputs, [f'_t_Asinh_{idx}_output'],
                               name=f"Asinh_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v9.Greater")
def Greater(A, B, **kwargs):
  _inputs = []
  for i in (A, B):
    _add_input(i, _inputs)

  idx = omm.op_counter["Greater"]
  omm.op_counter["Greater"] += 1
  node = onnx.helper.make_node("Greater",
                               _inputs, [f'_t_Greater_{idx}_C'],
                               name=f"Greater_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v9.Flatten")
def Flatten(input, **kwargs):
  _inputs = []
  for i in (input, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Flatten"]
  omm.op_counter["Flatten"] += 1
  node = onnx.helper.make_node("Flatten",
                               _inputs, [f'_t_Flatten_{idx}_output'],
                               name=f"Flatten_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v9.BatchNormalization")
def BatchNormalization(X, scale, B, mean, var, **kwargs):
  _inputs = []
  for i in (X, scale, B, mean, var):
    _add_input(i, _inputs)

  idx = omm.op_counter["BatchNormalization"]
  omm.op_counter["BatchNormalization"] += 1
  node = onnx.helper.make_node("BatchNormalization",
                               _inputs, [f'_t_BatchNormalization_{idx}_Y'],
                               name=f"BatchNormalization_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v9.Cosh")
def Cosh(input, **kwargs):
  _inputs = []
  for i in (input, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Cosh"]
  omm.op_counter["Cosh"] += 1
  node = onnx.helper.make_node("Cosh",
                               _inputs, [f'_t_Cosh_{idx}_output'],
                               name=f"Cosh_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v9.Cast")
def Cast(input, **kwargs):
  _inputs = []
  for i in (input, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Cast"]
  omm.op_counter["Cast"] += 1
  node = onnx.helper.make_node("Cast",
                               _inputs, [f'_t_Cast_{idx}_output'],
                               name=f"Cast_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v9.PRelu")
def PRelu(X, slope, **kwargs):
  _inputs = []
  for i in (X, slope):
    _add_input(i, _inputs)

  idx = omm.op_counter["PRelu"]
  omm.op_counter["PRelu"] += 1
  node = onnx.helper.make_node("PRelu",
                               _inputs, [f'_t_PRelu_{idx}_Y'],
                               name=f"PRelu_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v9.Atanh")
def Atanh(input, **kwargs):
  _inputs = []
  for i in (input, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Atanh"]
  omm.op_counter["Atanh"] += 1
  node = onnx.helper.make_node("Atanh",
                               _inputs, [f'_t_Atanh_{idx}_output'],
                               name=f"Atanh_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v9.MatMul")
def MatMul(A, B, **kwargs):
  _inputs = []
  for i in (A, B):
    _add_input(i, _inputs)

  idx = omm.op_counter["MatMul"]
  omm.op_counter["MatMul"] += 1
  node = onnx.helper.make_node("MatMul",
                               _inputs, [f'_t_MatMul_{idx}_Y'],
                               name=f"MatMul_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v9.Constant")
def Constant(**kwargs):
  _inputs = []
  for i in ():
    _add_input(i, _inputs)

  idx = omm.op_counter["Constant"]
  omm.op_counter["Constant"] += 1
  node = onnx.helper.make_node("Constant",
                               _inputs, [f'_t_Constant_{idx}_output'],
                               name=f"Constant_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v9.Less")
def Less(A, B, **kwargs):
  _inputs = []
  for i in (A, B):
    _add_input(i, _inputs)

  idx = omm.op_counter["Less"]
  omm.op_counter["Less"] += 1
  node = onnx.helper.make_node("Less",
                               _inputs, [f'_t_Less_{idx}_C'],
                               name=f"Less_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v9.Gemm")
def Gemm(A, B, C, **kwargs):
  _inputs = []
  for i in (A, B, C):
    _add_input(i, _inputs)

  idx = omm.op_counter["Gemm"]
  omm.op_counter["Gemm"] += 1
  node = onnx.helper.make_node("Gemm",
                               _inputs, [f'_t_Gemm_{idx}_Y'],
                               name=f"Gemm_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node
