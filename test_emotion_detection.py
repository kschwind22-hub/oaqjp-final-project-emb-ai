from EmotionDetection import emotion_detector

def test_emotion_detection():

    sentences = {
        "I am glad this happened": "joy",
        "I am really mad about this": "anger",
        "I feel disgusted just hearing about this": "disgust",
        "I am so sad about this": "sadness",
        "I am really afraid that this will happen": "fear"
    }

    for sentence, expected in sentences.items():
        result = emotion_detector(sentence)
        dominant = result['dominant_emotion']

        print("Text:", sentence)
        print("Expected:", expected)
        print("Detected:", dominant)

        if dominant == expected:
            print("PASS\n")
        else:
            print("FAIL\n")

test_emotion_detection()
