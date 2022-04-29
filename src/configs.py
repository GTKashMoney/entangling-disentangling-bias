import argparse

parser = argparse.ArgumentParser()

### COMMON
parser.add_argument('--device', default='cuda', type=str)
parser.add_argument('--lr', default=0.001, type=float, help='learning rate')
parser.add_argument('--alpha', default=0.25, type=float, help='EnD alpha')
parser.add_argument('--beta', default=0.75, type=float, help='EnD beta')
parser.add_argument('--weight_decay', default=1e-4, type=float, help='weight decay')
parser.add_argument('--batch_size', default=256, type=int, help='batch size')
parser.add_argument('--epochs', type=int, default=80)
parser.add_argument('--local', dest='local', action='store_true', help='disable wandb')
parser.add_argument('--unbias_val', action='store_true', help='cannot hyperparam tune')
parser.add_argument('--disable_end', action='store_true', help='remove EnD loss')
parser.add_argument('--load', default='', type=str, help='pass in file name to load model, i.e. model.pt')
parser.add_argument('--save', default='', type=str, help='pass in file name to save model, i.e. model.pt')

### REBIAS MNIST
parser.add_argument('--rho', type=float, default=0.997, help='rho for biased mnist (.999, .997, .995, .990)')

### COMMONS
parser.set_defaults(local=False)
config = parser.parse_args()
