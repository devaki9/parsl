# EIC

install in benc dev container with:

apt install elixir libzmq3-dev erlang-dev

then run:

pytest -s parsl/tests/ --config parsl/tests/configs/htex_elixir.py 

**TODO: Add description**

## Installation

If [available in Hex](https://hex.pm/docs/publish), the package can be installed
by adding `elixirchange` to your list of dependencies in `mix.exs`:

```elixir
def deps do
  [
    {:elixirchange, "~> 0.1.0"}
  ]
end
```

Documentation can be generated with [ExDoc](https://github.com/elixir-lang/ex_doc)
and published on [HexDocs](https://hexdocs.pm). Once published, the docs can
be found at <https://hexdocs.pm/elixirchange>.
