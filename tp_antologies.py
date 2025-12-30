from rdflib import Graph, Namespace, RDF, RDFS, OWL, BNode

# Création du graphe
g = Graph()

# Namespace
EX = Namespace("http://example.org/ontology#")
g.bind("ex", EX)
g.bind("owl", OWL)
g.bind("rdfs", RDFS)

# ======================
# Classes
# ======================
classes = [
    "Course",
    "LaboratoryCourse",
    "Homework",
    "Teacher",
    "Professor",
    "Assistant"
]

for cls in classes:
    g.add((EX[cls], RDF.type, OWL.Class))

# ======================
# Hiérarchie (is-a)
# ======================
g.add((EX.LaboratoryCourse, RDFS.subClassOf, EX.Course))
g.add((EX.Professor, RDFS.subClassOf, EX.Teacher))
g.add((EX.Assistant, RDFS.subClassOf, EX.Teacher))

# ======================
# Propriétés
# ======================
g.add((EX.partOf, RDF.type, OWL.ObjectProperty))
g.add((EX.organizedBy, RDF.type, OWL.ObjectProperty))
g.add((EX.teaches, RDF.type, OWL.ObjectProperty))

# Domaines et ranges
g.add((EX.partOf, RDFS.domain, EX.Homework))
g.add((EX.partOf, RDFS.range, EX.Course))

g.add((EX.organizedBy, RDFS.domain, EX.Course))
g.add((EX.organizedBy, RDFS.range, EX.Teacher))

g.add((EX.teaches, RDFS.domain, EX.Teacher))
g.add((EX.teaches, RDFS.range, EX.Course))

# ======================
# Contraintes logiques (OWL) — utiliser des BNode pour les restrictions
# ======================

# Professors teach only Courses
restriction_prof = BNode()
g.add((restriction_prof, RDF.type, OWL.Restriction))
g.add((restriction_prof, OWL.onProperty, EX.teaches))
g.add((restriction_prof, OWL.allValuesFrom, EX.Course))
g.add((EX.Professor, RDFS.subClassOf, restriction_prof))

# Assistants teach only LaboratoryCourses
restriction_asst = BNode()
g.add((restriction_asst, RDF.type, OWL.Restriction))
g.add((restriction_asst, OWL.onProperty, EX.teaches))
g.add((restriction_asst, OWL.allValuesFrom, EX.LaboratoryCourse))
g.add((EX.Assistant, RDFS.subClassOf, restriction_asst))

# ======================
# Sauvegarde
# ======================
if __name__ == "__main__":
    g.serialize(destination="ontology.owl", format="xml")
    print("Ontologie générée avec succès : ontology.owl")