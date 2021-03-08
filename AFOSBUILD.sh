rm -rf /opt/ANDRAX/bin/expliot
cp -Rf andraxbin/* /opt/ANDRAX/bin

chmod -R 755 /opt/ANDRAX/bin

export PYTHONPATH=/opt/ANDRAX/expliot/lib/python3.7/site-packages/

python3 setup.py install --prefix=/opt/ANDRAX/expliot
