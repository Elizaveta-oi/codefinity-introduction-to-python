# Initial items on shelf #1 (provided as a tuple)
shelf1 = ("celery", "spinach", "cucumbers")

# Items being added to the shelf #1 (provided as a list)
shelf1_update = ["tomatoes", "celery", "cilantro"]

shelf1_update_tuple = tuple(shelf1_update)

shelf1_concat = shelf1 + shelf1_update_tuple
print("Updated Shelf #1: ", shelf1_concat)

celery_count = shelf1_concat.count("celery")
print("Number of Celery: ",celery_count)

celery_index = shelf1_concat.index("celery")
print("Celery Index: ", celery_index)