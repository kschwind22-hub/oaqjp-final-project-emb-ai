python
mkdir EmotionDetection
mv emotion_detection.py EmotionDetection/
touch EmotionDetection/__init__.pynano EmotionDetection/__init__.pyfrom .emotion_detection import emotion_detector
python3
git add EmotionDetection/__init__.py EmotionDetection/emotion_detection.py
git commit -m "Package application as EmotionDetection"
git push origin main
pwd
ls
ls EmotionDetectionmkdir -p EmotionDetection
mv emotion_detection.py EmotionDetection/
echo "from .emotion_detection import emotion_detector" > EmotionDetection/__init__.py
git add EmotionDetection/__init__.py EmotionDetection/emotion_detection.py
git commit -m "Add EmotionDetection package"
git push origin main
git status
cd /home/project/final_project/oaqjp-final-project-emb-ai
find . -maxdepth 2 -type f
./EmotionDetection/__init__.py
./EmotionDetection/emotion_detection.py
ibm-developer-skills-network/oaqjp-final-project-emb-ai:main

