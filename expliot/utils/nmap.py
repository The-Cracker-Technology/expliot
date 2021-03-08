"""nmap utility."""

import xmltodict
from expliot.utils import Tool

NOTIMEOUT = 0


class Nmap(Tool):
    """
    Nmap tool execution class.
    """

    def __init__(self, path="nmap", default_args="-oX -"):
        """
        Initialize the Nmap Tool object

        Args:
            path(str): The full path (or the name) of nmap. Default
                is "nmap"
            default_args(str): Any default args that should always be
                part of the nmap arguments. Default is xml output argument
                "-oX -".
        """
        super().__init__(path, default_args=default_args)

    def run_xmltodict_output(self, args, timeout=None):
        """
        Run the command as a child with the specified arguments
        and return the output as a dict along with the error if any.
        The xml to dict format is generated by xmltodict package which
        is based on the format specified here -
        https://www.xml.com/pub/a/2006/05/31/converting-between-xml-and-json.html

        Args:
            args(str): The arguments to be supplied to nmap.
            timeout(int): The timeout in seconds while waiting
                for the output. Default is None. For details check
                subprocess.Popen() timeout argument.
        Returns:
            tuple of dict,str: Tuple of xml output converted to dict
                and error converted from bytes to str.
                (stdout,stderr)
        """
        out, err = self.run(args, timeout=timeout)
        err = err.decode() if err else None
        if not out:
            if not err:
                err = "No output received from nmap"
        else:
            out = xmltodict.parse(out, dict_constructor=dict)
        return (out, err)