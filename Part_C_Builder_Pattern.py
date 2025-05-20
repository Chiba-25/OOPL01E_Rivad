class Computer:
    #Represents a computer with configurable hardware components.
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.gpu = None

    def specs(self):
        #Returns the computer's specifications as a dictionary.
        return vars(self)

class ComputerBuilder:
    #Builder class to construct a Computer instance step-by-step.
    def __init__(self):
        self.reset()  # Initialize with a fresh Computer object

    def reset(self):
        #Resets the builder to start a new configuration.
        self.computer = Computer()
        return self

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def set_storage(self, storage):
        self.computer.storage = storage
        return self

    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def build(self):
        #Returns the configured Computer instance and resets the builder for reuse.
        built_computer = self.computer
        self.reset()  # Reset for the next build
        return built_computer

# Demo
builder = ComputerBuilder()

# Building a gaming PC
gaming_pc = builder.set_cpu("AMD Ryzen™ 9 9950X3D").set_ram("64GB").set_storage("8TB SSD").set_gpu("RTX 5090").build()
print("Gaming PC specs:", gaming_pc.specs())

# Reusing the builder to create a budget PC
budget_pc = builder.set_cpu("Intel Core i7 10700").set_ram("16GB").set_storage("512GB SSD").set_gpu("RTX 3060").build()
print("Budget PC specs:", budget_pc.specs())
