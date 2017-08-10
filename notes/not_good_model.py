import tensorflow as tf
class Model(object):
    """docstring for Model"""
    def __init__(self,data,target):
        data_size = int(data.get_shape()[1])
        target_size = int(target.get_shape()[1])
        weight = tf.Variable(tf.truncated_normal([data_size,target_size]))
        bias = tf.Variable(tf.constant(0.1,shape=[target_size]))
        incoming = tf.matmul(data,weight)+bias
        self._prediction = tf.nn.softmax(incoming)
        cross_entropy = -tf.reduce_sum(target,tf.log(self._prediction))
        self._optimize = tf.train.RMSPropOptimizer(0.03).minimize(cross_entropy)
        mistakes = tf.not_equal(tf.argmax(self._prediction,1),tf.argmax(target,1))
        self._error = tf.reduce_mean(tf.cast(tf.mistakes,tf.float32))
    @property
    def prediction(self):
        return self._prediction

    @property
    def optimize(self):
        return self._optimize

    @property
    def error(self):
        return self._error
"""
This is basically, how models are defined in the TensorFlow codebase. However, there are some problems with it. Most notably, the whole graph is define in a single function, the constructor. This is neither particularly readable nor reusable.
"""
