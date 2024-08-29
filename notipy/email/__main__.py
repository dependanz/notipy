import sys
import ast
import argparse

from .gmail import send_gmail

parser = argparse.ArgumentParser(
    prog = 'notipy.email',
    description = ''
)
parser.add_argument(
    '--source',
    required=True
)
parser.add_argument(
    '--destination',
    required=True
)
parser.add_argument(
    '--gmail_app_pass',
    default=None
)
parser.add_argument(
    '--label',
    default='notipy'
)
parser.add_argument(
    '--subject',
    default='Process Finished'
)
parser.add_argument(
    '--messages',
    nargs="*",
    default=None
)
parser.add_argument(
    'pipe_params',
    nargs="*"
)

args = parser.parse_args()
if not sys.stdin.isatty():
    args.pipe_params.extend(sys.stdin.read().splitlines())

#######################################
# Validate source domain credentials 
#######################################
source_domain = args.source.split('@')[-1]
destination_domain = args.destination.split('@')[-1]

if source_domain == 'gmail.com':
    assert args.gmail_app_pass is not None
    if args.messages is None:
        args.messages = []
    send_gmail(
        source       = args.source,
        destination  = args.destination,
        app_password = args.gmail_app_pass,
        label        = args.label,
        subject      = args.subject,
        messages     = [msg for msg in [*args.messages, *ast.literal_eval(repr(args.pipe_params))] if msg is not None]
    )
else:
    raise ValueError("Unsupported source address domain")