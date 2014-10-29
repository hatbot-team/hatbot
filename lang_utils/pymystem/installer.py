# -*- coding: utf-8 -*-
import platform
import os
import sys

from .constants import (MYSTEM_BIN, MYSTEM_EXE, MYSTEM_DIR)

_TARBALL_URLS = {
    'linux': {
        '32bit': "http://download.cdn.yandex.net/mystem/mystem-3.0-linux3.5-32bit.tar.gz",
        '64bit': "http://download.cdn.yandex.net/mystem/mystem-3.0-linux3.1-64bit.tar.gz",
    },
    'darwin': "http://download.cdn.yandex.net/mystem/mystem-3.0-macosx10.8.tar.gz",
    'win': {
        '32bit': "http://download.cdn.yandex.net/mystem/mystem-3.0-win7-32bit.zip",
        '64bit': "http://download.cdn.yandex.net/mystem/mystem-3.0-win7-64bit.zip",
    },
    'freebsd': {
        '64bit': "http://download.cdn.yandex.net/mystem/mystem-3.0-freebsd9.0-64bit.tar.gz",
    }
}


def autoinstall(out=sys.stderr):
    """
    Install mystem binary as :py:const:`~pymystem3.constants.MYSTEM_BIN`.
    Do nothing if already installed.
    """

    if os.path.isfile(MYSTEM_BIN):
        return
    install(out)


def install(out=sys.stderr):
    """
    Install mystem binary as :py:const:`~pymystem3.constants.MYSTEM_BIN`.
    Overwrite if already installed.
    """

    import requests
    import tempfile

    url = _get_tarball_url()

    print("Installing mystem to %s from %s" % (MYSTEM_BIN, url), file=out)

    if not os.path.isdir(MYSTEM_DIR):
        os.makedirs(MYSTEM_DIR)

    tmp_fd, tmp_path = tempfile.mkstemp()
    try:
        r = requests.get(url, stream=True)
        with os.fdopen(tmp_fd, 'wb') as fd:
            for chunk in r.iter_content(64 * 1024):
                fd.write(chunk)
            fd.flush()

        if url.endswith('.tar.gz'):
            import tarfile
            with tarfile.open(tmp_path) as tar:
                tar.extract(MYSTEM_EXE, MYSTEM_DIR)
        elif url.endswith('.zip'):
            import zipfile
            with zipfile.ZipFile(tmp_path) as zip:
                zip.extractall(MYSTEM_DIR)
        else:
            raise NotImplementedError("Could not install mystem from %s" % url)
    finally:
        os.unlink(tmp_path)


def _get_on_prefix(kvs, key):
    for k, v in kvs.items():
        if key.startswith(k):
            return v
    return None


def _get_tarball_url():
    bits, _ = platform.architecture()

    url = _get_on_prefix(_TARBALL_URLS, sys.platform)
    if url is None:
        raise NotImplementedError("Your system is not supported. Feel free to report bug or make a pull request.")

    if isinstance(url, str):
        return url

    url = url.get(bits, None)
    if url is None:
        raise NotImplementedError("Your system is not supported. Feel free to report bug or make a pull request.")

    return url

