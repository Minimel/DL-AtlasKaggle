import tensorflow as tf
from base.base_model import BaseModel


class CBDP4Model(BaseModel):
    def __init__(self, config):
        super(CBDP4Model, self).__init__(config)
        self.build_model()
        self.init_saver()

    def build_model(self):
        super(CBDP4Model, self).init_build_model()
        print(self.input_layer.get_shape())
        # Block 1 - 64
        x = tf.layers.conv2d(self.input_layer, 32, 3,
                             padding='same', name='conv1')
        x = tf.layers.batch_normalization(
            x, training=self.is_training, name='bn1')
        x = tf.nn.relu(x, name='act1')
        x = tf.layers.dropout(x, rate=0.5, training=self.is_training)
        x = tf.layers.max_pooling2d(
            x, pool_size=(2, 2), strides=(2, 2), name='pool1')
        print(x.get_shape())
        # Block 2 - 128
        x = tf.layers.conv2d(x, 64, 3, padding='same', name='conv2')
        x = tf.layers.batch_normalization(
            x, training=self.is_training, name='bn2')
        x = tf.nn.relu(x, name='act2')
        x = tf.layers.dropout(x, rate=0.5, training=self.is_training)
        x = tf.layers.max_pooling2d(
            x, pool_size=(2, 2), strides=(2, 2), name='pool2')
        print(x.get_shape())
        # Block 3 - 256
        x = tf.layers.conv2d(x, 128, 3, padding='same', name='conv3')
        x = tf.layers.batch_normalization(
            x, training=self.is_training, name='bn3')
        x = tf.nn.relu(x, name='act3')
        x = tf.layers.dropout(x, rate=0.5, training=self.is_training)
        x = tf.layers.max_pooling2d(
            x, pool_size=(2, 2), strides=(2, 2), name='pool3')
        print(x.get_shape())
        # Block 4 - 256
        x = tf.layers.conv2d(x, 256, 3, padding='same', name='conv4')
        x = tf.layers.batch_normalization(
            x, training=self.is_training, name='bn4')
        x = tf.nn.relu(x, name='act4')
        x = tf.layers.dropout(x, rate=0.5, training=self.is_training)
        x = tf.layers.max_pooling2d(
            x, pool_size=(2, 2), strides=(2, 2), name='pool4')
        print(x.get_shape())
        # Classification block
        x = tf.layers.flatten(x, name='flatten')
        x = tf.nn.relu(x, name='act5')
        self.logits = tf.layers.dense(x, units=28, name='logits')

        super(CBDP4Model, self).build_loss_output()

    def init_saver(self):
        # here you initialize the tensorflow saver that will be used
        # in saving the checkpoints.
        self.saver = tf.train.Saver(max_to_keep=self.config.max_to_keep)
