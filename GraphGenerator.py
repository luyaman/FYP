import snap
from diffusion.IndependentCascade import ICDiffusion
from seedSelection.DegreeSelection import HighDegreeSelection
from seedSelection.DistanceCentralitySelection import DistanceCentralitySelection

# LoadEdgeList(graphType, inputFileName, sourceNodeColumnId, destinationNodeColumnId, separator)
facebook = snap.LoadEdgeList(snap.PUNGraph, "graphs/facebook_combined.txt", 0, 1)
print(facebook.GetNodes())

selection = DistanceCentralitySelection(facebook, 10)
seeds = selection.select()
print("Seed set: ")
print(seeds)
print("\nInfluence: ")
print(ICDiffusion(facebook, seeds, 0.01).cal_expected())


dselection = HighDegreeSelection(facebook, 15)
dseeds = dselection.select()
print("\nSeed set: ")
print(dseeds)
print("\nInfluence: ")
print(ICDiffusion(facebook, dseeds, 0.05).cal_expected())
