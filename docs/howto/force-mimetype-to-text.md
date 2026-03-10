# Force mime type to text

The following `.gitignore` is for example considered
binary by dotdrop since its mime type is `application/x-wine-extension-ini`

```
[user]
        name = user
        email = user@example.com

[credential]
        helper = cache
```

Dotdrop can be forced to consider specific mime types as text.
Set the following environment variable:
```bash
export DOTDROP_MIME_TEXT=application/x-wine-extension-ini
```

see [environment variables](../usage.md#environment-variables)
