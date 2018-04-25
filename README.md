# chainer-bbox
Using SSD 300 example included in ChainerCV, we will detect objects of handwritten graphics.

# dependency
```console
pip install cupy chainer
pip install -U numpy
pip install chainercv==0.8.0
```
# install
```console
git clone https://github.com/kfjt/chainer-bbox.git
```

# run demo
```console
wget https://github.com/kfjt/chainer-bbox/releases/download/v1.0/model.zip
unzip model.zip -d chainer-bbox

cd chainer-bbox
python demo.py --gpu 0 all.png
```
