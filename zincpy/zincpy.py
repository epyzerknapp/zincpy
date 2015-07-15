__author__ = 'epyzerknapp'

import urllib, urllib2
import warnings



class ZincParser:
    """
    This is the base class for the Zinc parser in ZincPy.
    """
    def __init__(self, logfile=False):
        """
        Initialization of the ZincParser object
        :param logfile: The name of the file which any logging will be written to.  If False, no logging is performed.
        :return:
        """
        self.base_url = "http://zinc.docking.org/results/combination"
        self.config = {'structure.similarity': 1.00,
              'filter.purchasability': 'all','page.format': 'smiles',
              'protomer.molwt.max':1000.0,'protomer.molwt.min':0.0,
              'protomer.rotbond.max':7}
        self.loglevel = 0
        self.logfile = logfile

    def set_search_parameters(self, config):
        """
        Use this function to set the parameters for the scrape.
        It is possible to set to search a specific smiles string, or to instead search on properties.
        If a smiles string is not supplied, a warning is raised. This can be
        Set any values which are different to the default configurations.
        The default values are:
        'structure.similarity': 1.00,
        'filter.purchasability': 'all',
        'page.format': 'smiles',
        'protomer.molwt.max':1000.0,
        'protomer.molwt.min':0.0,
        'protomer.rotbond.max':7
        :return:
        """
        for k, v in config.items():
            self.config[k] = v

    def search(self):
        """
        This function is the call to execute the search
        :return:
        """
        if 'structure.smiles' not in self.config.keys():
            warnings.warn('No smiles string has been detected')
        config = urllib.urlencode(self.config)
        request = urllib2.Request(self.base_url, config)
        response = urllib2.urlopen(request)
        info = response.read()
        return response2dict(info)

    def search_smiles_list(self, smiles_list):
        """
        This function is a wrapper to easily search Zinc through a list of smiles strings.
        :param smiles_list:
        :return: Dict, key = smiles, value = response from ZINC
        """
        all_info = dict()
        for smi in smiles_list:
            self.set_search_parameters({'structure.smiles':smi})
            info = self.search()
            all_info[smi] = info
        return all_info


def response2dict(response):
    """
    This converts the response from urllib2's call into a dict
    :param response:
    :return:
    """
    split_newlines = response.split('\r\n')
    split_tabs = [s.split('\t') for s in split_newlines if s !='']
    return split_tabs