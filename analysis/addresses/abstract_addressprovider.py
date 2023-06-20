from analysis.src.AddressFinderRegExp import AddressFinderRegExp


# This is the abstract base class for address providers.
# It provides a common structure for subclasses to implement.
class AbstractAddressProvider:

    def __init__(self, bit_mask_finder: AddressFinderRegExp = None):
        # Constructor method for the AbstractAddressProvider class.
        # It takes an optional bit_mask_finder parameter.
        # This parameter is used for finding addresses based on signatures.
        self.bit_mask_finder = bit_mask_finder

    def getValues(self) -> []:
        # Abstract method to be implemented by subclasses.
        # It should return a dictionary or a list of values.
        # Subclasses must override this method.
        raise NotImplementedError("Subclasses must implement the getValues method.")
