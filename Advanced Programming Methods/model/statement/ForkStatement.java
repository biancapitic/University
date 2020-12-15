package model.statement;

import model.ProgramState;
import model.adt.*;
import model.value.StringValue;
import model.value.Value;

import java.io.BufferedReader;

public class ForkStatement implements Statement{

    private final Statement statement;

    public ForkStatement(Statement statement) {
        this.statement = statement;
    }

    public Statement getStatement() {
        return statement;
    }

    @Override
    public ProgramState execute(ProgramState programState) {

        IStack<Statement> executionStack = new MyStack<>();
        IDictionary<String, Value> newSymbolTable = new MyDictionary<String, Value>();
        programState.getSymbolTable().getContent()
                .forEach((key, value) -> newSymbolTable.update(key, value.deepCopy()));

        synchronized (programState.getFileTable()) {
            synchronized (programState.getHeap()) {
                synchronized (programState.getOutput()) {
                    IDictionary<StringValue, BufferedReader> fileTable = programState.getFileTable();
                    IHeap<Value> heap = programState.getHeap();
                    IList<Value> output = programState.getOutput();

                    return new ProgramState(executionStack, newSymbolTable, output, this.statement, fileTable, heap);
                }
            }
        }
    }

    @Override
    public Statement deepCopy() {
        return new ForkStatement(this.statement.deepCopy());
    }

    @Override
    public String toString() {
        return "fork(" + this.statement + ")";
    }
}
