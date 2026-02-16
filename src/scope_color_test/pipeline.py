from typing import TYPE_CHECKING

import torch

from scope.core.pipelines.interface import Pipeline, Requirements

from .schema import ColorTestConfig

if TYPE_CHECKING:
    from scope.core.pipelines.base_schema import BasePipelineConfig


class ColorTestPipeline(Pipeline):
    """Simple color overlay/blend pipeline for testing."""

    @classmethod
    def get_config_class(cls) -> type["BasePipelineConfig"]:
        return ColorTestConfig

    def __init__(self, device: torch.device | None = None, **kwargs):
        self.device = (
            device
            if device is not None
            else torch.device("cuda" if torch.cuda.is_available() else "cpu")
        )

    def prepare(self, **kwargs) -> Requirements:
        """We need exactly one input frame per call."""
        return Requirements(input_size=1)

    def __call__(self, **kwargs) -> dict:
        """Blend a solid color with input video frames."""
        video = kwargs.get("video")
        if video is None:
            raise ValueError("ColorTestPipeline requires video input")

        # Stack input frames -> (T, H, W, C) and normalize to [0, 1]
        frames = torch.stack([frame.squeeze(0) for frame in video], dim=0)
        frames = frames.to(device=self.device, dtype=torch.float32) / 255.0

        # Read runtime parameters from kwargs
        red = kwargs.get("red", 1.0)
        green = kwargs.get("green", 1.0)
        blue = kwargs.get("blue", 1.0)
        alpha = kwargs.get("alpha", 0.5)

        # Create solid color tensor matching frame dimensions
        T, H, W, C = frames.shape
        color = torch.zeros((T, H, W, C), device=self.device, dtype=torch.float32)
        color[..., 0] = red    # Red channel
        color[..., 1] = green  # Green channel
        color[..., 2] = blue   # Blue channel

        # Blend: original video * (1 - alpha) + color * alpha
        result = frames * (1.0 - alpha) + color * alpha

        return {"video": result.clamp(0, 1)}
