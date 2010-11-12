all: prenom.py resource_rc.py

prenom.py: prenom.ui
	pyuic4 prenom.ui > prenom.py
resource_rc.py: resource.qrc nounours_cropped.png
	pyrcc4 resource.qrc > resource_rc.py
