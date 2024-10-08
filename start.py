import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from dp import dp, bot
import views

if __name__ == "__main__":
    import asyncio
    asyncio.run(dp.start_polling(bot))
