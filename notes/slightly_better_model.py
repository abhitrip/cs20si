import tensorflow as tf
class Model(object):
    """docstring for Model"""
    def __init__(self,data,target):
        self.data = data
        self.target = target
        self._prediction = None
        self._optimize = None
        self._error = None
    @property
    def prediction(self):
        if not self._prediction:
            data_size = int(self.data.get_shape()[1])
            target_size = int(self.target.get_shape()[1])
            weight = tf.Variable(tf.truncated_normal([data_size,target_size]))
            bias = tf.Variable(tf.constant(0.1,shape=[target_size]))
            incoming = tf.matmul(self.data,weight)+bias
            self._prediction = tf.nn.softmax(incoming)
        return self._prediction
    @property
    def optimize(self):
        if not self._optimize:
            cross_entropy = -tf.reduce_sum(self.target,tf.log(self.prediction))
            optimizer = tf.train.RMSPropOptimizer(0.03)
            self._optimize = optimizer.minimize(cross_entropy)
        return self._optimize

    @property
    def error(self):
        if not self._error:
            mistakes = tf.not_equal(
                tf.argmax(self.target, 1), tf.argmax(self.prediction, 1))
            self._error = tf.reduce_mean(tf.cast(mistakes, tf.float32))
        return self._error
"""
This is much better than the first example. Your code now is structured into functions that you can focus on individually. However, the code is still a bit bloated due to the lazy-loading logic. Let’s see how we can improve on that.
"""
