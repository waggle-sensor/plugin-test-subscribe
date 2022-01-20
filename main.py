#!/usr/bin/env python3
import argparse
import subprocess
import logging


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true", help="enable debug logging")
    parser.add_argument("--pywaggle-ref", default="HEAD", type=str, help="pywaggle ref to use")
    parser.add_argument("topics", nargs="+", type=str, help="topics to subscribe to")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.debug else logging.INFO,
        format="%(asctime)s %(message)s",
        datefmt="%Y/%m/%d %H:%M:%S",
    )

    subprocess.check_call(["git", "clone", "http://github.com/waggle-sensor/pywaggle"])
    subprocess.check_call(["git", "-C", "pywaggle", "checkout", args.pywaggle_ref])
    subprocess.check_call(["pip3", "install", "-q", "./pywaggle"])

    from waggle.plugin import Plugin

    logging.info("setting up plugin")
    with Plugin() as plugin:
        logging.info("subscribing to %s", args.topics)
        plugin.subscribe(*args.topics)

        logging.info("waiting for values")
        while True:
            logging.info("got value %s", plugin.get())



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
