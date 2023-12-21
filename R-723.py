class FavoritesList:
    def __init__(self):
        # initialize the list and any other necessary variables

    def reset_counts(self):
        # Reset all elements' access counts to zero
        for element in self.list:
            element.access_count = 0

    # Other methods and variables of FavoritesList class