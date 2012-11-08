all: prenom.py resource_rc.py results.py

prenom.py: prenom.ui
	pyuic4 prenom.ui > prenom.py
results.py: results.ui
	pyuic4 results.ui > results.py
resource_rc.py: resource.qrc nounours_cropped.png icon.png
	pyrcc4 -py3 resource.qrc > resource_rc.py

clean:
	rm prenom.py resource_rc.py results.py
