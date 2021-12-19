import wandb
import os

def init_wandb(cfg: dict, model, args=None) -> None:
    """Initialize project on Weights & Biases
    Args:
        cfg (dict): Configuration dictionary
    """
    wandb.init(
        name=args.version,
        project="ynet",
        config=cfg,
        dir="~/",
    )
    if args:
        wandb.config.update(args)

    wandb.watch(model, log="all")

def save_model_wandb(save_path: str):
    """Save model weights to wandb
    """
    wandb.save(os.path.abspath(save_path))

def log_losses(loss: dict, mode: str, epoch: int):
    """
    Log the losses
    Args:
        losses (dict): all the losses should be of type float
        mode (str): "train" or "val"
        epoch (int): epoch number
    """
    wandb.log({f"{mode}_loss": loss}, step=epoch)


def log_metrics(metric: dict, mode: str, epoch: int):
    """
    Log the metrics
    Args:
        metrics (dict): all the metrics should be of type float
        mode (str): "train" or "val"
        epoch (int): epoch number
    """

    for k, v in metrics.items():
        wandb.log({f"{mode}/{k}": v}, step=epoch)

def log_summary(best_metrics: dict):
    
    for key in best_metrics:
        wandb.run.summary[f"{key}"] = best_metrics[key]