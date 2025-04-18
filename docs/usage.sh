# check
python3 docs/concat.py
code temp.txt

# install
python3 -m pip install --upgrade twine
python3 -m pip install --upgrade build

# config
code $HOME/.pypirc

# editable
python3 -m pip install --editable .

# build
rm -rf ./dist && python3 -m build
tar -tf dist/hanjadict-0.3.1.tar.gz

# test
python3 -m twine upload --repository testpypi dist/* --verbose
python3 -m pip install --force -U --index-url https://test.pypi.org/simple/ --no-deps hanjadict
python3 docs/pip_test.py

# production
python3 -m twine upload dist/* --verbose
python3 -m pip install --force -U hanjadict
