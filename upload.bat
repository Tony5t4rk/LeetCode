call conda activate base
python "./readme-generator.py"
git add .
git commit -m "update daily"
git push origin master