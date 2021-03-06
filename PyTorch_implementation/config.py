class Config(object):
   def __init__(self,
                lr_dis=0.0001, lr_gen=0.001, n_epochs=10, batch_size=14,
                use_L1_loss=True, lambda_L1 = 10,
                image_size=256,
                train_dir='/labs/gevaertlab/data/momena/lfw/', model_dir='model_params/', test_dir='testing_data/', prediction_dir='prediction_data/', predicted_dir='predicted_data/',
                save_frequency=10,
                gpu=0):

      self.lr_dis = lr_dis
      self.lr_gen = lr_gen
      self.n_epochs = n_epochs
      self.batch_size = batch_size

      self.use_L1_loss = use_L1_loss
      self.lambda_L1 = lambda_L1

      self.image_size = image_size

      self.model_dir = model_dir
      self.train_dir = train_dir
      self.test_dir = test_dir
      self.prediction_dir = prediction_dir
      self.predicted_dir = predicted_dir
      self.save_frequency = save_frequency

      self.gpu = gpu