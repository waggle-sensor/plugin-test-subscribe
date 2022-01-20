# Plugin Test Subscribe

Internal plugin to help perform system testing of Waggle Edge Stack.

## Usage

```sh
pluginctl run --name test-subscribe waggle/plugin-test-subscribe:0.1.2 [--debug] [--pywaggle-ref github-ref] topics...
```

This will install pywaggle from HEAD or the provided ref and run a plugin which subscribes to the provided topics.

## Examples

The following will install pywaggle 0.52.7 and subscribe to all env.* topics.

```sh
pluginctl run --name test-subscribe waggle/plugin-test-subscribe:0.1.2 --pywaggle-ref 0.52.7 'env.*'
```
