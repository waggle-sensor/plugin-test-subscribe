# Plugin Test Subscribe

Internal plugin to help perform system testing of Waggle Edge Stack.

## Usage

```sh
pluginctl run plugin-test-subscribe:0.1.0 [--debug] [--pywaggle-ref github-ref] topics...
```

This will install pywaggle from HEAD or the provided ref and run a plugin which subscribes to the provided topics.
