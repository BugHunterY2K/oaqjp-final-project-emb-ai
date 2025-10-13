from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
       
        joy_test = emotion_detector('I am glad this happened')
        self.assertEqual(joy_test['dominant_emotion'], 'joy')

        anger_test = emotion_detector('I am really mad about this')
        self.assertEqual(anger_test['dominant_emotion'], 'anger')

        disgust_test = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(disgust_test['dominant_emotion'], 'disgust')

        sadness_test = emotion_detector('I am so sad about this')
        self.assertEqual(sadness_test['dominant_emotion'], 'sadness')

        fear_test = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(fear_test['dominant_emotion'], 'fear')
      
unittest.main()