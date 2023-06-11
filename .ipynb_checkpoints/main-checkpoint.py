print('start')

import tensorflow as tf

print('imported')

(X_tr, y_tr), (X_te, y_te) = tf.keras.datasets.fashion_mnist.load_data()

print('done')