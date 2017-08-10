import tensorflow as tf



def basic_addition():
    a = tf.constant(2)
    b = tf.constant(3)
    x = tf.add(a,b)
    with tf.Session() as sess:
        writer = tf.summary.FileWriter('./graphs',sess.graph)
        print(sess.run(x))

    writer.close()

def addition_with_naming():
    a = tf.constant([2,2],name='a')
    b = tf.constant([3,6],name='b')
    x = tf.add(a,b,name='add')
    with tf.Session() as sess:
        writer = tf.summary.FileWriter('./graphs',sess.graph)
        print(sess.run(x))
    writer.close()

def create_specific_tensors():
    zeros = tf.zeros([2,3],tf.int32) # Same with ones
    temp = tf.constant([[1,2],[2,3],[4,5]]) # Same with ones
    zeros_like = tf.zeros_like(temp) # Same with ones
    fill = tf.fill([2,3],8)
    linspace = tf.linspace(10.0,13.0,4,name='linspace')
    range_ = tf.range(start=1,limit=1,delta=-0.5)
    random = tf.random_normal([2,3],mean=0,stddev=0.1)
    with tf.Session() as sess:
        print("zeros: "+str(sess.run(zeros)))
        print("zeros_like: "+str(sess.run(zeros_like)))
        print("fill: "+str(sess.run(fill)))
        print("linspace: "+str(sess.run(linspace)))
        print("range_: "+str(sess.run(range_)))
        print("random: "+str(sess.run(random)))

def explore_protobuff():
    my_const = tf.constant([1.0,2.0],name='my_const')
    print(tf.get_default_graph().as_graph_def())

def explore_variables():
    a = tf.Variable(2,name='scalar')
    b = tf.Variable(tf.truncated_normal([2,3]),name='vector')
    c = tf.Variable(b.initialized_value()*2)
    a_times_2 = a.assign(a*2)
    init = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.run(init)
        #sess.run(a.initializer)
        print("a:"+str(sess.run(a)))
        print("a:"+str(sess.run(a_times_2)))
        print("a:"+str(sess.run(a.assign_add(2))))
        print("a:"+str(sess.run(a.assign_sub(2))))
        sess.run(init)
        print("b:"+str(sess.run(b)))
        print("c:"+str(sess.run(c)))


def explore_placeholders():
    a = tf.placeholder(tf.float32,shape=[3])
    b = tf.constant([5,5,5],tf.float32)
    c = a+b
    with tf.Session() as sess:
        print(sess.run(c,feed_dict={a:[1,2,3]}))

def normal_loading():
    x = tf.Variable(10,name='x')
    y = tf.Variable(5,name='y')
    z = tf.add(x,y)
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        writer = tf.summary.FileWriter('./graphs',sess.graph)
        for _ in range(10):
            sess.run(z)
        writer.close()
    print(tf.get_default_graph().as_graph_def())

def lazy_loading():
    x = tf.Variable(10,name='x')
    y = tf.Variable(5,name='y')
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        writer = tf.summary.FileWriter('./graphs',sess.graph)
        for _ in range(10):
            sess.run(tf.add(x,y))
        writer.close()
    print(tf.get_default_graph().as_graph_def())


if __name__=="__main__":
    #basic_addition()
    #addition_with_naming()
    #create_specific_tensors()
    #explore_protobuff()
    #explore_variables()
    #explore_placeholders()
    normal_loading()
    #lazy_loading()
